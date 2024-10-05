import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { useProducts, useCurrentTime } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';
import '@testing-library/jest-dom';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(),
    useCurrentTime: jest.fn(),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(),
    updateCategories: jest.fn(),
}));

jest.mock('../../components/Categories', () => ({
    Categories: ({ selectedCategories, onCategoryClick }: any) => (
        <div data-testid="categories">
            <button onClick={() => onCategoryClick('Электроника')}>
                Электроника
            </button>
            <button onClick={() => onCategoryClick('Одежда')}>Одежда</button>
        </div>
    ),
}));

jest.mock('../../components/ProductCard', () => ({
    ProductCard: ({ name }: any) => <div>{name}</div>,
}));

describe('MainPage Component', () => {
    const mockProducts = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iPhone model',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Гусь костюм',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ];

    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(mockProducts);
        (useCurrentTime as jest.Mock).mockReturnValue('12:00:00');
        (applyCategories as jest.Mock).mockImplementation(
            (products, categories) => {
                if (categories.length === 0) return products;
                return products.filter((product: { category: any; }) =>
                    categories.includes(product.category)
                );
            }
        );
        (updateCategories as jest.Mock).mockImplementation(
            (currentCategories, clickedCategory) => {
                if (currentCategories.includes(clickedCategory)) {
                    return currentCategories.filter(
                        (category: any) => category !== clickedCategory
                    );
                }
                return [...currentCategories, clickedCategory];
            }
        );
    });

    it('should render the main title and current time', () => {
        render(<MainPage />);
        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        expect(screen.getByText('12:00:00')).toBeInTheDocument(); // Mocked current time
    });

    it('should render all products initially', () => {
        render(<MainPage />);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    it('should filter products based on selected categories', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();

        fireEvent.click(screen.getByText('Электроника'));

        expect(applyCategories).toHaveBeenCalledWith(mockProducts, [
            'Электроника',
        ]);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.queryByText('Костюм гуся')).not.toBeInTheDocument();

        fireEvent.click(screen.getByText('Одежда'));

        expect(applyCategories).toHaveBeenCalledWith(mockProducts, [
            'Электроника',
            'Одежда',
        ]);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    it('should deselect a category when clicked again', () => {
        render(<MainPage />);

        fireEvent.click(screen.getByText('Электроника'));

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.queryByText('Костюм гуся')).not.toBeInTheDocument();

        fireEvent.click(screen.getByText('Электроника'));

        expect(applyCategories).toHaveBeenCalledWith(mockProducts, []);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });
});

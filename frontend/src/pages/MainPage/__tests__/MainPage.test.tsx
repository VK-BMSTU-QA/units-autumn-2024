import React from 'react';
import '@testing-library/jest-dom';
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { useCurrentTime, useProducts } from '../../../hooks';
import { Product } from '../../../types';
import { Categories } from '../../../components/Categories';

jest.mock('../../../hooks', () => ({
    useCurrentTime: jest.fn(),
    useProducts: jest.fn(),
}));

jest.mock('../../../components/Categories', () => ({
    Categories: jest.fn(() => <div>Categories component</div>),
    ProductCard: jest.fn(({ name }) => <div>{name}</div>),
}));

describe('MainPage', () => {
    const mockProducts: Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ];

    beforeEach(() => {
        (useCurrentTime as jest.Mock).mockReturnValue('12:00');
        (useProducts as jest.Mock).mockReturnValue(mockProducts);
    });

    it('should display title and current time', () => {
        render(<MainPage />);

        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        expect(screen.getByText('12:00')).toBeInTheDocument();
    });

    it('should display Categories component', () => {
        render(<MainPage />);

        expect(screen.getByText('Categories component')).toBeInTheDocument();
    });

    it('should display a set of products with ProductCard', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    it('should update chosen categories after button pressing', () => {
        const mockOnCategoryClick = jest.fn();

        (Categories as jest.Mock).mockImplementation(({ onCategoryClick }) => (
            <button onClick={() => onCategoryClick('Электроника')}>
                Электроника
            </button>
        ));

        render(<MainPage />);

        const categoryButton = screen.getByRole('button', {
            name: 'Электроника',
        });
        fireEvent.click(categoryButton);

        expect(mockOnCategoryClick).not.toHaveBeenCalled();

        // Продукты обновляются после клика по категории
        expect(screen.queryByText('Костюм гуся')).not.toBeInTheDocument();
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('should display all products if no category choose', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });
});

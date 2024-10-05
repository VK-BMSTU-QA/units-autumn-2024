import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { Category, Product } from '../../types';
import { applyCategories, getPrice, updateCategories } from '../../utils';
import { useCurrentTime } from '../../hooks';

jest.mock('../../utils');
jest.mock('../../hooks');
jest.mock('../../components', () => ({
    Categories: (props: {
        selectedCategories: Category[];
        onCategoryClick: (category: Category) => void;
    }) => (
        <div>
            {categories.map((category, idx) => (
                <div
                    key={idx}
                    onClick={() => props.onCategoryClick?.(category)}
                    className={
                        props.selectedCategories.includes(category)
                            ? 'selected'
                            : ''
                    }
                >
                    {category}
                </div>
            ))}
        </div>
    ),
    ProductCard: (product: Product) => <div>{product.name}</div>,
}));

const categories: Category[] = ['Одежда', 'Для дома', 'Электроника'];

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const products: Product[] = [
            {
                id: 1,
                name: 'Продукт 1',
                description: 'Описание продукта 1',
                price: 100,
                priceSymbol: '₽',
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Продукт 2',
                description: 'Описание продукта 2',
                price: 200,
                priceSymbol: '₽',
                category: 'Для дома',
            },
        ];

        jest.mocked(applyCategories).mockReturnValue(products);

        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.getByText('VK Маркет')).toBeInTheDocument();
    });

    it('should display date', () => {
        jest.mocked(useCurrentTime).mockReturnValue('2024-10-04');

        const rendered = render(<MainPage />);

        expect(rendered.queryAllByText('2024-10-04').length).toEqual(1);
    });

    it('should display categories', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getAllByText('Электроника').length).toBeGreaterThan(0);
        expect(rendered.getAllByText('Для дома').length).toBeGreaterThan(0);
    });

    it('should display filter on category', () => {
        jest.mocked(updateCategories).mockReturnValue(['Электроника']);

        const rendered = render(<MainPage />);
        const categoryBtn = rendered.getAllByText('Электроника')[0];

        fireEvent.click(categoryBtn);

        expect(rendered.getByText('Одежда')).not.toHaveClass('selected');
        expect(rendered.getByText('Электроника')).toHaveClass('selected');
        expect(rendered.getByText('Для дома')).not.toHaveClass('selected');
    });
});

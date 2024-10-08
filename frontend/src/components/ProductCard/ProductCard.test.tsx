import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

enum mockCategory {
    Clothing = 'Одежда',
}

const mockProduct = {
    id: 1,
    name: 'p1',
    description: 'd1',
    price: 1,
    imgUrl: '1',
    category: mockCategory.Clothing,
};

jest.mock('../../utils/getPrice');

describe('ProductCard test', () => {
    beforeEach(() => {
        (getPrice as jest.Mock).mockImplementation(
            (value: number) => `${value} ₽`
        );
    });
    afterEach(() => {
        jest.clearAllMocks();
    });

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...mockProduct} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display product details correctly', () => {
        const rendered = render(<ProductCard {...mockProduct} />);
        expect(rendered.getByText(mockProduct.name)).toBeInTheDocument();
        expect(rendered.getByText(mockProduct.description)).toBeInTheDocument();
        expect(
            rendered.getByText(getPrice(mockProduct.price))
        ).toBeInTheDocument();
        expect(rendered.getByText(mockProduct.category)).toBeInTheDocument();
        expect(rendered.getByAltText(mockProduct.name)).toBeInTheDocument();
    });
    // точная проверка: ищется элемент и в нем ищется совпадение
    it('should display product name correctly', () => {
        const rendered = render(<ProductCard {...mockProduct} />);
        const nameElement = rendered.getByRole('heading', {
            name: mockProduct.name,
        });
        expect(nameElement).toBeInTheDocument();
    });
});

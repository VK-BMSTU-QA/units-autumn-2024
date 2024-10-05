import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';
jest.mock('../../utils');
afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    const productMock: Product = {
        name: 'Название тестового продукта',
        description: 'Описание тестового продукта',
        price: 1234567,
        priceSymbol: '₽',
        category: 'Электроника',
        imgUrl: 'https://example.com/image.jpg',
        id: 0,
    };
    it('should be displayed correctly', () => {
        jest.mocked(getPrice).mockReturnValue('1234567 ₽');
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('product name should be displayed correctly', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.name)).toBeInTheDocument();
    });
    it('product description should be displayed correctly', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.description)).toBeInTheDocument();
    });
    it('price should be displayed', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText('1234567 ₽')).toBeInTheDocument();
    });
    it('product categort should be displayed', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.category)).toBeInTheDocument();
    });
    it('product image should be displayed while using imgUrl', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByAltText(productMock.name)).toBeInTheDocument();
    });
    it('product image should not be displayed while not using imgUrl', () => {
        const productWithoutImage = { ...productMock, imgUrl: undefined };
        const rendered = render(<ProductCard {...productWithoutImage} />);
        expect(
            rendered.queryByAltText(productMock.name)
        ).not.toBeInTheDocument();
    });
});
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
        name: 'Тестовый продукт',
        description: 'Описание тестового продукта',
        price: 100,
        priceSymbol: '₽',
        category: 'Электроника',
        imgUrl: 'https://example.com/image.jpg',
        id: 0,
    };

    it('should render correctly', () => {
        jest.mocked(getPrice).mockReturnValue('100 ₽');

        const rendered = render(<ProductCard {...productMock} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display product name', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.name)).toBeInTheDocument();
    });

    it('should display product description', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.description)).toBeInTheDocument();
    });

    it('should display product price', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText('100 ₽')).toBeInTheDocument();
    });

    it('should display product category', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.category)).toBeInTheDocument();
    });

    it('should display product image when imgUrl is provided', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByAltText(productMock.name)).toBeInTheDocument();
    });

    it('should not display product image when imgUrl is not provided', () => {
        const productWithoutImage = { ...productMock, imgUrl: undefined };
        const rendered = render(<ProductCard {...productWithoutImage} />);
        expect(
            rendered.queryByAltText(productMock.name)
        ).not.toBeInTheDocument();
    });

    it('should call getPrice function with correct arguments', () => {
        render(<ProductCard {...productMock} />);
        expect(jest.mocked(getPrice)).toHaveBeenCalledWith(
            productMock.price,
            productMock.priceSymbol
        );
    });
});

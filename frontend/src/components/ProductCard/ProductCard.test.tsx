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
    it('должен отображаться корректно', () => {
        jest.mocked(getPrice).mockReturnValue('1234567 ₽');
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('должно отображаться название продукта', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.name)).toBeInTheDocument();
    });
    it('должно отображаться описание продукта', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.description)).toBeInTheDocument();
    });
    it('должна отображаться цена продукта', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText('1234567 ₽')).toBeInTheDocument();
    });
    it('должна отображаться категория продукта', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByText(productMock.category)).toBeInTheDocument();
    });
    it('должно отображаться изображение продукта при использовании imgUrl', () => {
        const rendered = render(<ProductCard {...productMock} />);
        expect(rendered.getByAltText(productMock.name)).toBeInTheDocument();
    });
});
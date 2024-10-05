import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);

let productWithImg : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
    imgUrl: '/iphone.png'
}

let productWithoutImg : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
}

describe('product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard key={productWithoutImg.id} {...productWithoutImg}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly with img', () => {
        const rendered = render(<ProductCard key={productWithImg.id} {...productWithImg}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
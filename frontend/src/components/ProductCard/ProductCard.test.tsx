import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);

let product : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
}

let productWithNoPic : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
    imgUrl: '/iphone.png'
}

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard key={product.id} {...product}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly with img', () => {
        const rendered = render(<ProductCard key={productWithNoPic.id} {...productWithNoPic}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});

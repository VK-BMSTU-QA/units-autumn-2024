import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from "../../types";

describe('ProductCard test', () => {
    const product: Product = {
        id: 1,
        name: 'Product 1',
        description: 'best product',
        price: 777,
        priceSymbol: '₽',
        category: 'Для дома',
        imgUrl: '/product.png',
    };

    it('should render correctly', () => {
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const productWithoutImg = { ...product, imgUrl: undefined };
        const { asFragment } = render(<ProductCard {...productWithoutImg} />);
        expect(asFragment()).toMatchSnapshot();
    });
});

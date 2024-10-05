import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';
import type { Product } from '../../types/Product';

jest.mock('../../utils', () => ({
    getPrice: jest.fn(),
}));

const product: Product = {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iPhone, buy it now!',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
};

describe('ProductCard component', () => {
    it('should render product details correctly', () => {
        (getPrice as jest.Mock).mockReturnValue('999 $');
        render(<ProductCard {...product} />);

        expect(screen.getByText(product.name)).toBeInTheDocument();
        expect(screen.getByText(product.description)).toBeInTheDocument();
        expect(screen.getByText('999 $')).toBeInTheDocument();
        expect(screen.getByText(product.category)).toBeInTheDocument();
        expect(screen.getByAltText(product.name)).toBeInTheDocument();
    });

    it('should not render image when imgUrl is not provided', () => {
        const productWithoutImage: Product = { ...product, imgUrl: undefined };

        render(<ProductCard {...productWithoutImage} />);

        expect(screen.queryByAltText(productWithoutImage.name)).not.toBeInTheDocument();
    });

    it('should render product without price symbol if priceSymbol is not provided', () => {
        const productWithoutSymbol: Product = { ...product, priceSymbol: undefined };
        (getPrice as jest.Mock).mockReturnValue('999'); 
        render(<ProductCard {...productWithoutSymbol} />);

        expect(getPrice).toHaveBeenCalledWith(product.price, undefined);
        expect(screen.getByText('999')).toBeInTheDocument();
    });
});

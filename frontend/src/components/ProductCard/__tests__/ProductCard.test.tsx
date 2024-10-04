import React from 'react';
import { render, screen } from '@testing-library/react';
import { ProductCard } from '../ProductCard';
import { getPrice } from '../../../utils';
import { Product } from '../../../types/Product';
import '@testing-library/jest-dom';

// Замокаем getPrice
jest.mock('../../../utils', () => ({
    getPrice: jest.fn((value, symbol) => `${symbol}${value}`),
}));

describe('ProductCard', () => {
    const product: Product = {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    };

    it('должен отобразить название продукта', () => {
        render(<ProductCard {...product} />);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('должен отобразить описание продукта', () => {
        render(<ProductCard {...product} />);
        expect(
            screen.getByText('Latest iphone, buy it now')
        ).toBeInTheDocument();
    });

    it('должен отобразить цену продукта с символом валюты', () => {
        render(<ProductCard {...product} />);
        expect(screen.getByText('$999')).toBeInTheDocument();
        expect(getPrice).toHaveBeenCalledWith(999, '$');
    });

    it('должен отобразить категорию продукта', () => {
        render(<ProductCard {...product} />);
        expect(screen.getByText('Электроника')).toBeInTheDocument();
    });

    it('должен отобразить изображение продукта, если оно есть', () => {
        render(<ProductCard {...product} />);
        const image = screen.getByAltText('IPhone 14 Pro');
        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', '/iphone.png');
    });

    it('не должен отображать изображение, если его нет', () => {
        const productWithoutImage = { ...product, imgUrl: undefined };
        render(<ProductCard {...productWithoutImage} />);
        expect(screen.queryByAltText('IPhone 14 Pro')).not.toBeInTheDocument();
    });
});

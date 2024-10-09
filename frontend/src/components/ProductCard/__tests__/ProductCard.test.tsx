import React from 'react';
import { Product } from '../../../types/Product';
import { ProductCard } from '../ProductCard';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';

describe('product card test', () => {
    const products: Product = {
        id: 2,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1000,
        priceSymbol: '₽',
        category: 'Одежда',
    };

    test('должен быть костюм гуся', () => {
        render(<ProductCard {...products} />);
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    test('должен отобразить цену с символом валюты', () => {
        render(<ProductCard {...products} />);
        expect(screen.getByText('1 000 ₽')).toBeInTheDocument();
    });

    test('должна быть категория одежда', () => {
        render(<ProductCard {...products} />);
        expect(screen.getByText('Одежда')).toBeInTheDocument();
    });

    test('не должна отображаться картинка если ее нет', () => {
        const productWithoutImg = { ...products, imgUrl: undefined};
        render(<ProductCard {...productWithoutImg} />);
        expect(screen.queryByAltText('Костюм гуся')).not.toBeInTheDocument();
    });
});

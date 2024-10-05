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

    test('', () => {
        render(<ProductCard {...products} />);
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    })

    test('', () => {
        render(<ProductCard {...products} />);
        expect(screen.getByText('Одежда')).toBeInTheDocument();
    })
});
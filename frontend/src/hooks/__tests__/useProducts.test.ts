import { renderHook } from '@testing-library/react';
import { useProducts } from '../useProducts';
import { Product } from '../../types';

describe('useProducts', () => {
    it('должен возвращать массив продуктов', () => {
        const { result } = renderHook(() => useProducts());

        const expectedProducts: Product[] = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ];

        expect(result.current).toEqual(expectedProducts);
    });

    it('должен возвращать корректное количество продуктов', () => {
        const { result } = renderHook(() => useProducts());

        expect(result.current).toHaveLength(4);
    });

    it('должен содержать продукт с категорией "Электроника"', () => {
        const { result } = renderHook(() => useProducts());

        const electronicsProduct = result.current.filter(
            (product: Product) => product.category === 'Электроника'
        );

        expect(electronicsProduct).toHaveLength(2); // Должно быть 2 продукта с категорией "Электроника"
    });

    it('должен содержать продукт с ценой 1000 ₽', () => {
        const { result } = renderHook(() => useProducts());

        const productWithPrice = result.current.find(
            (product: Product) => product.price === 1000 && product.priceSymbol === '₽'
        );

        expect(productWithPrice).toBeDefined();
        expect(productWithPrice?.name).toBe('Костюм гуся');
    });
});

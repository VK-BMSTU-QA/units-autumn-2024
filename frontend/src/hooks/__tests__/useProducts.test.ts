import { renderHook } from '@testing-library/react';
import { useProducts } from '../useProducts';

describe('useProducts hook', () => {
    const expectedProducts = [
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
        }
    ];

    it('should return an array of products', () => {
        const { result } = renderHook(() => useProducts());

        expect(Array.isArray(result.current)).toBe(true);
        expect(result.current.length).toBe(expectedProducts.length);

        expectedProducts.forEach((product, index) => {
            expect(result.current[index]).toEqual(product);
        });
    });

    it('should return products with correct category', () => { 
        const { result } = renderHook(() => useProducts());
        result.current.forEach(product => {
            expect(['Электроника', 'Одежда', 'Для дома']).toContain(product.category);
        });
    });
});

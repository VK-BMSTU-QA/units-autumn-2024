import { renderHook } from '@testing-library/react';
import { useProducts } from '../useProducts';

describe('useProducts hook', () => {
    it('should return an array of products', () => {
        const { result } = renderHook(() => useProducts());
        expect(Array.isArray(result.current)).toBe(true);
        expect(result.current.length).toBe(4); 

        expect(result.current[0]).toEqual({
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        });

        expect(result.current[1]).toEqual({
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        });

        expect(result.current[2]).toEqual({
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        });

        expect(result.current[3]).toEqual({
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        });
    });

    it('should return products with correct price and category', () => {
        const { result } = renderHook(() => useProducts());

        result.current.forEach(product => {
            expect(typeof product.price).toBe('number');
            expect(['Электроника', 'Одежда', 'Для дома']).toContain(product.category);
        });
    });
});

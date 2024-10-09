import { useProducts } from "../useProducts";
import { renderHook } from "@testing-library/react";
import { Product } from "../../types";

describe('test use products function', () => {
    test('должен возвращаться массив продуктов', () => {
        const { result } = renderHook(() => useProducts());

        const expected: Product[] = [
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

        expect(result.current).toEqual(expected);
    });

    test('Должен содержать продукт с названием Настольная лампа', () => {
        const { result } = renderHook(() => useProducts());

        const expected = result.current.filter(
            (product: Product) => product.name === 'Настольная лампа'
        );
    });

    test('должно возвращаться корректное кол-во продуктов', () => {
        const { result } = renderHook(() => useProducts());

        expect(result.current).toHaveLength(4);
    });

    test('должен содержать продукт с категорией Для дома', () => {
        const { result } = renderHook(() => useProducts());

        const houseProd = result.current.filter(
            (product: Product) => product.category === 'Для дома'
        );

        expect(houseProd).toHaveLength(1);
    });

    test('проверка на содержание цены', () => {
        const { result } = renderHook(() => useProducts());

        const productPrice = result.current.find(
            (product: Product) => product.price === 999 && product.priceSymbol === '$'
        );

        expect(productPrice).toBeDefined();
        expect(productPrice?.name).toBe('IPhone 14 Pro');
    })
});

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

    test('Должен содержать продукт с названием Micro Tunnel Boring Machine', () => {
        const { result } = renderHook(() => useProducts());

        const expected = result.current.filter(
            (product: Product) => product.name === 'Micro Tunnel Boring Machine'
        );
    });

    test('должно возвращаться корректное кол-во продуктов', () => {
        const { result } = renderHook(() => useProducts());

        expect(result.current).toHaveLength(4);
    })
});

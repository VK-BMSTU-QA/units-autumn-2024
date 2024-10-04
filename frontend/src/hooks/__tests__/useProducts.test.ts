import { useProducts } from "../useProducts";
import { renderHook } from "@testing-library/react";
import { Product } from "../../types";

describe('test use products function', () => {
    test('должен возвращаться массив продуктов', () => {
        const { result } = renderHook(() => useProducts());

        const expected: Product[] = [
            {
                id: 1,
                name: 'Cargo Landing Craft',
                description: 'For navy units',
                price: 1000,
                priceSymbol: '$',
                category: 'Одежда',
            },
            {
                id: 2,
                name: 'Mma Toughest Training Cage Martial Art Cage Mma Octagon Boxing Fintess Center',
                description: 'proffesional equipment',
                price: 399,
                priceSymbol: '₽',
                category: 'Для дома',
            },
            {
                id: 3,
                name: 'Micro Tunnel Boring Machine',
                description: 'for young experimenters',
                price: 9999,
                priceSymbol: '$',
                category: 'Для дома',
            },
            {
                id: 4,
                name: 'Pizza Vending Machine',
                description: 'A smart pizza vending machine',
                price: 1337,
                priceSymbol: '₽',
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

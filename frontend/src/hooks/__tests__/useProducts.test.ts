import {useProducts} from "../useProducts";
import {renderHook} from "@testing-library/react";
describe('test useProducts hook', () => {
    it('should return an array of products', () => {
        const { result } = renderHook(() => useProducts());
        const products = result.current;

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
            },
        ];

        expect(products).toStrictEqual(expectedProducts);
    });
    it('should return another array of products', () => {
        const { result } = renderHook(() => useProducts());
        const products = result.current;

        const expectedProducts = [
            {
                id: 2,
                name: 'IPhone 16 Pro',
                description: 'xiaomi better',
                price: 999999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone16.png',
            },
            {
                id: 3,
                name: 'Костюм улитки',
                description: 'Запускаем улитку, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
            {
                id: 1,
                name: 'Подстольная лампа',
                description: 'Говорят, что ее использовали в disney',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Факс',
                description: 'Незаменимая вещь для школьника',
                price: 7000,
                category: 'Электроника',
            },
        ];

        expect(products).not.toStrictEqual(expectedProducts);
    });
});
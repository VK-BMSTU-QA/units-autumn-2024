import { applyCategories } from "../applyCategories";
import type { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const products: Product[] = [
        {id: 1, name: 'Куртец', description: 'Я этот куртец в последний раз одевал в девяносто четвертом, на стрелку', price: 666, category: 'Одежда'},
        {id: 2, name: 'Long Range Reconnaissance Drone With Fixed Wings', description: 'wtf', price: 100, category: 'Электроника'},
        {id: 3, name: 'Холодильник', description: 'Источник холодного пива', price: 200, category: 'Для дома'},
    ];

    test('если категории не указаны, должен вернуть все продукты', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    test('если категория указана, возвращает продукты из этой категории', () => {
        const result = applyCategories(products, ['Одежда']);
        expect(result).toEqual([
            {id: 1, name: 'Куртец', description: 'Я этот куртец в последний раз одевал в девяносто четвертом, на стрелку', price: 666, category: 'Одежда'},
        ]);
    });

});
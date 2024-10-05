import { applyCategories } from '../applyCategories';
import type { Product, Category } from '../../types';

describe('test apply categories function', () => {
    const products: Product[] = [
        {
            id: 1,
            name: 'Смартфон',
            description: 'Новый смартфон',
            price: 50000,
            category: 'Электроника',
        },
        {
            id: 2,
            name: 'Плед',
            description: 'Уютный плед',
            price: 2000,
            category: 'Для дома',
        },
        {
            id: 3,
            name: 'Кофемашина',
            description: 'Автоматическая кофемашина',
            price: 15000,
            category: 'Для дома',
        },
        {
            id: 4,
            name: 'Шуба',
            description: 'Зимняя шуба',
            price: 30000,
            category: 'Одежда',
        },
    ];

    it('should return all products when categories array is empty', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('should filter products by given categories', () => {
        const categories: Category[] = ['Электроника', 'Для дома'];
        const expectedResult = products.filter((product) =>
            categories.includes(product.category)
        );
        const result = applyCategories(products, categories);
        expect(result).toEqual(expectedResult);
    });

    it('should return array when products match categories', () => {
        const categories: Category[] = ['Одежда', 'Игрушки'] as Category[];
        const result = applyCategories(products, categories);
        expect(result).toEqual([
            {
                id: 4,
                name: 'Шуба',
                description: 'Зимняя шуба',
                price: 30000,
                category: 'Одежда',
            },
        ]);
    });

    it('should return all products when single matching category is provided', () => {
        const categories: Category[] = ['Электроника'];
        const expectedResult = products.filter(
            (product) => product.category === 'Электроника'
        );
        const result = applyCategories(products, categories);
        expect(result).toEqual(expectedResult);
    });
});

import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('applyCategories', () => {
    const products: Product[] = [
        { id: 1, name: 'Телефон', description: 'Смартфон', price: 1000, category: 'Электроника' },
        { id: 2, name: 'Пылесос', description: 'Пылесос для дома', price: 500, category: 'Для дома' },
        { id: 3, name: 'Футболка', description: 'Хлопковая футболка', price: 100, category: 'Одежда' },
    ];

    it('должен вернуть все продукты, если категории не указаны', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('должен вернуть продукты только из категории Электроника', () => {
        const result = applyCategories(products, ['Электроника']);
        expect(result).toEqual([
            { id: 1, name: 'Телефон', description: 'Смартфон', price: 1000, category: 'Электроника' },
        ]);
    });

    it('должен вернуть продукты из категорий Электроника и Для дома', () => {
        const result = applyCategories(products, ['Электроника', 'Для дома']);
        expect(result).toEqual([
            { id: 1, name: 'Телефон', description: 'Смартфон', price: 1000, category: 'Электроника' },
            { id: 2, name: 'Пылесос', description: 'Пылесос для дома', price: 500, category: 'Для дома' },
        ]);
    });

    it('должен вернуть продукты только из категории Одежда', () => {
        const result = applyCategories(products, ['Одежда']);
        expect(result).toEqual([
            { id: 3, name: 'Футболка', description: 'Хлопковая футболка', price: 100, category: 'Одежда' },
        ]);
    });
});

import { applyCategories } from '../applyCategories';
import type { Product, Category } from '../../types';
describe('test apply categories function', () => {
    const products: Product[] = [
    {
        id: 1,
        name: 'Ipad Pro',
        description: 'Новый высокопроизводительный планшет с большим экраном и мощным процессором',
        price: 55000,
        category: 'Электроника',
    },
    {
        id: 2,
        name: 'Палка-хваталка',
        description: 'Позволяет хватать предметы, для которых не хватает длины рук',
        price: 2500,
        category: 'Для дома',
    },
    {
        id: 3,
        name: 'Робот пылесос',
        description: 'Автоматическая роботизированная машина по уборки вашего дома для всасывания пыли и сора с пола',
        price: 18000,
        category: 'Для дома',
    },
    {
        id: 4,
        name: 'Зимний меховой плащ',
        description: 'Теплый и изящный зимний плащ с натуральным мехом',
        price: 32000,
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
                name: 'Зимний меховой плащ',
                description: 'Теплый и изящный зимний плащ с натуральным мехом',
                price: 32000,
                category: 'Одежда',
            },
        ]);
    });
    it('should return all items if the only suitable category is specified', () => {
        const categories: Category[] = ['Электроника'];
        const expectedResult = products.filter(
            (product) => product.category === 'Электроника'
        );
        const result = applyCategories(products, categories);
        expect(result).toEqual(expectedResult);
    });
});
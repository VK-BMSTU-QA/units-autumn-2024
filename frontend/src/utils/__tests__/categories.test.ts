import { applyCategories } from '../applyCategories';
import { updateCategories } from '../updateCategories';
import { useProducts } from '../../hooks';

describe('test applyCategories function', () => {
    const products = useProducts();

    // при пустом массиве категорий должны вернуться все продукты
    it('should return products without changes if categories array is empty', () => {
        expect(applyCategories(products, [])).toEqual(products);
    });
    // 1 категория = 1 продукт
    it('should return products with only one category', () => {
        const expected = products.filter(
            (product) => product.category === 'Одежда'
        );
        expect(applyCategories(products, ['Одежда'])).toEqual(expected);
    });

    // все категории = все продукты
    it('should return products with all categories', () => {
        expect(
            applyCategories(products, ['Одежда', 'Для дома', 'Электроника'])
        ).toEqual(products);
    });
});

describe('test updateCategories function', () => {
    // убрать категорию, если она уже есть в массиве
    it('should remove category from array if it is already in array', () => {
        expect(updateCategories(['Одежда', 'Для дома'], 'Одежда')).toEqual([
            'Для дома',
        ]);
    });
    // добавить категорию, если она отсутствует
    it('should add category to array if it is not there', () => {
        expect(updateCategories(['Одежда', 'Для дома'], 'Электроника')).toEqual(
            ['Одежда', 'Для дома', 'Электроника']
        );
    });
    // добавить категорию в пустой массив
    it('should return array with category if it is added to empty array', () => {
        expect(updateCategories([], 'Одежда')).toEqual(['Одежда']);
    });
});

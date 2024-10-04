import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('updateCategories', () => {
    let categories: Category[];

    beforeEach(() => {
        categories = ['Электроника', 'Для дома', 'Одежда'];
    });

    it('должен добавить категорию, если ее нет в текущем списке', () => {
        const result = updateCategories([], 'Электроника');
        expect(result).toEqual(['Электроника']);
    });

    it('должен удалить категорию, если она уже присутствует в текущем списке', () => {
        const result = updateCategories(categories, 'Электроника');
        expect(result).toEqual(['Для дома', 'Одежда']);
    });

    it('должен добавить категорию, если ее нет в текущем списке', () => {
        const result = updateCategories(['Одежда'], 'Для дома');
        expect(result).toEqual(['Одежда', 'Для дома']);
    });

    it('должен корректно работать с пустым списком', () => {
        const result = updateCategories([], 'Одежда');
        expect(result).toEqual(['Одежда']);
    });
});

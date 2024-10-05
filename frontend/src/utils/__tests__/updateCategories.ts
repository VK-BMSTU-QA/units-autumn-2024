import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('updateCategories', () => {

    test('adds a category if it is not in the current categories', () => {
        const currentCategories: Category[] = ['Электроника', "Одежда"];
        const result = updateCategories(currentCategories, "Для дома");
        expect(result).toEqual(['Электроника', "Одежда", "Для дома"]);
    });

    test('removes a category if it is already in the current categories', () => {
        const currentCategories: Category[] = ['Электроника', "Одежда", "Для дома"];
        const result = updateCategories(currentCategories, "Одежда");
        expect(result).toEqual(['Электроника', "Для дома"]);
    });

    test('returns a new array and does not mutate the original array', () => {
        const currentCategories: Category[] = ['Электроника', "Одежда"];
        const result = updateCategories(currentCategories, "Для дома");
        expect(result).not.toBe(currentCategories);
        expect(currentCategories).toEqual(['Электроника', "Одежда"]);
    });
});

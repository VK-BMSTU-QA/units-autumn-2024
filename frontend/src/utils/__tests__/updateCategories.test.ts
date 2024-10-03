import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('updateCategories', () => {
    it('should add a category to the list', () => {
        const currentCategories: Category[] = ['Одежда', 'Для дома'];
        const changedCategories: Category = 'Электроника';
        const result = updateCategories(currentCategories, changedCategories);
        expect(result).toEqual(['Одежда', 'Для дома', 'Электроника']);
    });

    it('should remove a category from the list', () => {
        const currentCategories: Category[] = ['Одежда', 'Для дома'];
        const changedCategories: Category = 'Для дома';
        const result = updateCategories(currentCategories, changedCategories);
        expect(result).toEqual(['Одежда']);
    });
});

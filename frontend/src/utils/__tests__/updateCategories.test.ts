import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('Testing the updateCategories function', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома', 'Одежда'];

    it('should remove an existing category from the array if it exists', () => {
        const changedCategory: Category = 'Электроника';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toHaveLength(2);
        expect(result).not.toContain(changedCategory);
    });

    it('should modify the array', () => {
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).not.toStrictEqual(currentCategories);
    });

    it('should add to array only one item', () => {
        const result = updateCategories([], 'Одежда');
        expect(result).toHaveLength(1);
        expect(result).toContain('Одежда');
    });
});

import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('Testing the updateCategories function', () => {
    const initialCategories: Category[] = ['Для дома', 'Одежда'];

    it('should add a new category if it is not present in the array', () => {
        const newCategory: Category = 'Электроника';
        const updatedCategories = updateCategories(
            initialCategories,
            newCategory
        );
        expect(updatedCategories).toHaveLength(3);
        expect(updatedCategories).toContain(newCategory);
    });

    it('should remove an existing category from the array', () => {
        const existingCategory: Category = 'Для дома';
        const updatedCategories = updateCategories(
            initialCategories,
            existingCategory
        );
        expect(updatedCategories).toHaveLength(1);
        expect(updatedCategories).not.toContain(existingCategory);
    });

    it('should return an array with one category if it is empty and a new category is added', () => {
        const result = updateCategories([], 'Одежда');
        expect(result).toHaveLength(1);
        expect(result).toContain('Одежда');
    });
});

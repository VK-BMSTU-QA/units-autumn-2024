import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';
describe('test updateCategories function', () => {
  const initialCategories: Category[] = ['Электроника', 'Для дома'];

  // Тест на добавление новой категории
  it('should add a new category if it does not exist in the current categories', () => {
    const newCategory: Category = 'Одежда';
    const expectedCategories = [...initialCategories, newCategory];
    const result = updateCategories(initialCategories, newCategory);
    expect(result).toEqual(expectedCategories);
  });

  // Тест на удаление существующей категории
  it('should delete the existing category', () => {
    const existingCategory: Category = 'Электроника';
    const expectedCategories = initialCategories.filter(category => category !== existingCategory);
    const result = updateCategories(initialCategories, existingCategory);
    expect(result).toEqual(expectedCategories);
  });
});
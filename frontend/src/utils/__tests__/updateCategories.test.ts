import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';
describe('test updateCategories function', () => {
  const initialCategories: Category[] = ['Электроника', 'Для дома'];

  // Тест на добавление новой категории
  it('следует добавить новую категорию, если она не существует в текущих категориях', () => {
    const newCategory: Category = 'Одежда';
    const expectedCategories = [...initialCategories, newCategory];
    const result = updateCategories(initialCategories, newCategory);
    expect(result).toEqual(expectedCategories);
  });

  // Тест на удаление существующей категории
  it('следует удалить существующую категорию при повторном добавлении', () => {
    const existingCategory: Category = 'Электроника';
    const expectedCategories = initialCategories.filter(category => category !== existingCategory);
    const result = updateCategories(initialCategories, existingCategory);
    expect(result).toEqual(expectedCategories);
  });
});
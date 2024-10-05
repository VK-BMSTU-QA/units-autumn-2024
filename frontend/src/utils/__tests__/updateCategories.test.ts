import {updateCategories} from "../updateCategories";
import {Category} from "../../types";

describe("test update categories function", ()=>{
   it('should remove the category if it already exists', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома', 'Одежда'];
    const changedCategories: Category = 'Одежда';
    const expectedCategories: Category[] = ['Электроника', 'Для дома'];

    expect(updateCategories(currentCategories, changedCategories)).toEqual(expectedCategories);
  });
   it('should add the category if it not already exists', () => {
    const currentCategories: Category[] = ['Электроника', 'Одежда'];
    const changedCategories: Category = 'Для дома';
    const expectedCategories: Category[] = ['Электроника', 'Одежда', 'Для дома'];

    expect(updateCategories(currentCategories, changedCategories)).toEqual(expectedCategories);
  });
   it('should not modify the original array', () => {
    const currentCategories: Category[] = ['Одежда', 'Для дома'];
    const changedCategories: Category = 'Электроника';

    updateCategories(currentCategories, changedCategories);

    expect(currentCategories).toEqual(['Одежда', 'Для дома']);
  });
});
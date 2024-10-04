import { updateCategories } from "../updateCategories";
import { Category } from "../../types";

describe('test update categories function', () => {

    test('должен добавить категорию если она отсутствует в текущем списке', () => {
        const result = updateCategories([], 'Одежда');
        expect(result).toEqual(['Одежда']);
    });

    test('должен удалить категорию, если она уже есть в текущем списке', () => {
        const result = updateCategories(['Для дома', 'Электроника'], 'Для дома');
        expect(result).toEqual(['Электроника']);
    });

});
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Categories } from './Categories';

afterEach(jest.clearAllMocks);
describe('Categories test', () => {
    it('должен отображаться корректно', () => {
        const rendered = render(<Categories selectedCategories={[]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('следует добавить класс для выбранного значка - Одежда', () => {
        const rendered = render(<Categories selectedCategories={['Одежда']} />);

        expect(rendered.getByText('Одежда')).toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
            'categories__badge_selected'
        );
    });

    it('следует добавить класс для выбранного значка - Электроника', () => {
        const rendered = render(<Categories selectedCategories={['Электроника']} />);

        expect(rendered.getByText('Одежда')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
            'categories__badge_selected'
        );
    });

    it('следует добавить класс для выбранного значка - Для дома', () => {
        const rendered = render(<Categories selectedCategories={['Для дома']} />);

        expect(rendered.getByText('Одежда')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Электроника')).not.toHaveClass(
            'categories__badge_selected'
        );
        expect(rendered.getByText('Для дома')).toHaveClass(
            'categories__badge_selected'
        );
    });

    it('следует вызвать колбек при нажатии на категорию', () => {
        const onCategoryClick = jest.fn();
        const rendered = render(
            <Categories
                selectedCategories={[]}
                onCategoryClick={onCategoryClick}
            />
        );

        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
    });
});

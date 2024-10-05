import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Categories } from './Categories';

afterEach(jest.clearAllMocks);

describe('Categories test', () => {
    it('should be displayed correctly', () => {
        const rendered = render(<Categories selectedCategories={[]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for selected badge - Одежда', () => {
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

    it('should add class for selected badge - Электроника', () => {
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

    it('should add class for selected badge - Для дома', () => {
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

    it('should call the callback when clicked on category', () => {
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

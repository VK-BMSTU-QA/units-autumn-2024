import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Categories } from './Categories';

afterEach(jest.clearAllMocks);

describe('test Categories', () => {
    it('should render correctly', () => {
        const { asFragment } = render(<Categories selectedCategories={[]} />);

        expect(asFragment()).toMatchSnapshot();
    });

    it('should add class for selected badge', () => {
        const { getByText } = render(<Categories selectedCategories={['Одежда']} />);


        expect(getByText('Одежда')).toHaveClass('categories__badge_selected');
        expect(getByText('Для дома')).not.toHaveClass('categories__badge_selected');
        expect(getByText('Электроника')).not.toHaveClass('categories__badge_selected');

    });

    it('should call callback when category click', () => {
        const onCategoryClick = jest.fn();
        const { getByText } = render(
            <Categories selectedCategories={[]} onCategoryClick={onCategoryClick} />
        );


        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
    });
});

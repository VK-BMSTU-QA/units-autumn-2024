import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';

jest.mock('../../utils');
jest.mock('../../hooks');

describe('test MainPage', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    it('should render', () => {
        jest.mocked(applyCategories).mockReturnValue([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
        jest.mocked(useCurrentTime).mockReturnValue('12:00:00');

        const rendered = render(<MainPage />);
        expect(rendered).toMatchSnapshot();
    });

    it('should update categories', () => {
        jest.mocked(updateCategories).mockImplementation(
            (selected, clicked) => [...selected, clicked]
        );

        const rendered = render(<MainPage />);

        const categoryBtn = rendered.getByText('Для дома', {
            selector: '.categories__badge',
        });

        fireEvent.click(categoryBtn);

        expect(updateCategories).toHaveBeenCalledWith([], 'Для дома');
        expect(
            rendered.getByText('Для дома', {
                selector: '.categories__badge',
            })
        ).toHaveClass('categories__badge_selected');
    });

    it('should call useCurrentTime', () => {
        render(<MainPage />);

        expect(useCurrentTime).toHaveBeenCalled();
    });

    it('should call useProducts', () => {
        render(<MainPage />);

        expect(useProducts).toHaveBeenCalled();
    });
});

import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';
import { Product } from '../../types';

jest.mock('../../utils');
jest.mock('../../hooks');

describe('MainPage component tests', () => {
    const mockProducts: Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iPhone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ];

    beforeEach(() => {
        jest.mocked(applyCategories).mockReturnValue(mockProducts);
        jest.mocked(useCurrentTime).mockReturnValue('12:00:00');
        jest.mocked(updateCategories).mockImplementation(
            (activeCategories, clickedCategory) =>
                activeCategories.includes(clickedCategory)
                    ? activeCategories.filter(category => category !== clickedCategory)
                    : [...activeCategories, clickedCategory]
        );
    });

    it('renders the page and matches snapshot', () => {
        const { asFragment } = render(<MainPage />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('calls hooks useCurrentTime and useProducts', () => {
        render(<MainPage />);
        expect(useCurrentTime).toHaveBeenCalled();
        expect(useProducts).toHaveBeenCalled();
    });

    it('adds category when clicked', () => {
        const { getByText } = render(<MainPage />);
        const electronicsCategory = getByText('Электроника', { selector: '.categories__badge' });
        
        fireEvent.click(electronicsCategory);
        
        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');
        expect(electronicsCategory).toHaveClass('categories__badge_selected');
    });

    it('removes category when clicked again', () => {
        const { getByText } = render(<MainPage />);
        const electronicsCategory = getByText('Электроника', { selector: '.categories__badge' });

        fireEvent.click(electronicsCategory);
        fireEvent.click(electronicsCategory);

        expect(updateCategories).toHaveBeenCalledWith(['Электроника'], 'Электроника');
        expect(electronicsCategory).not.toHaveClass('categories__badge_selected');
    });
});

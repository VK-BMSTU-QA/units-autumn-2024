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
    });

    it('renders the page correctly', () => {
        const { asFragment } = render(<MainPage />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('calls the useCurrentTime hook', () => {
        render(<MainPage />);
        expect(useCurrentTime).toHaveBeenCalled();
    });

    it('calls the useProducts hook', () => {
        render(<MainPage />);
        expect(useProducts).toHaveBeenCalled();
    });

    it('should correctly update categories when clicked and remove category on second click', () => {
        jest.mocked(updateCategories).mockImplementation(
            (activeCategories, clickedCategory) => {
                if (activeCategories.includes(clickedCategory)) {
                    return activeCategories.filter(category => category !== clickedCategory);
                }
                return [...activeCategories, clickedCategory];
            }
        );
    
        const { getByText } = render(<MainPage />);
    
        const electronicsCategory = getByText('Электроника', {
            selector: '.categories__badge',
        });
    
        fireEvent.click(electronicsCategory);
        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');
        expect(
            getByText('Электроника', { selector: '.categories__badge' })
        ).toHaveClass('categories__badge_selected');
    
        fireEvent.click(electronicsCategory);
        expect(updateCategories).toHaveBeenCalledWith(['Электроника'], 'Электроника');
        expect(
            getByText('Электроника', { selector: '.categories__badge' })
        ).not.toHaveClass('categories__badge_selected');
    });
    
});

import { fireEvent, render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from '../MainPage';
import { useCurrentTime, useProducts } from '../../../hooks';
import { applyCategories, updateCategories } from '../../../utils';

jest.mock('../../../utils');
jest.mock('../../../hooks');

describe('Main Page tests', () => {
    it('should render correctly', () => {
        jest.mocked(applyCategories).mockReturnValue([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Последний iphone, купи его сейчас',
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
        ]);
        jest.mocked(useCurrentTime).mockReturnValue('12:00:00');
        const rendered = render(<MainPage />);
        expect(rendered).toMatchSnapshot();
    });

    it('should use useCurrentTime', () => {
        render(<MainPage />);
        expect(useCurrentTime).toHaveBeenCalled();
    });

    it('should use useProducts', () => {
        render(<MainPage />);
        expect(useProducts).toHaveBeenCalled();
    });

    it('should update categories when clicked', () => {
        jest.mocked(updateCategories).mockImplementation(
            (selected, clicked) => [...selected, clicked]
        );

        const rendered = render(<MainPage />);
        const categoryBtn = screen.getByText('Электроника', {
            selector: '.categories__badge',
        });

        fireEvent.click(categoryBtn);

        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');
        expect(
            screen.getByText('Электроника', {
                selector: '.categories__badge',
            })
        ).toHaveClass('categories__badge_selected');
    });
});


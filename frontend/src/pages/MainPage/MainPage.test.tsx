import { fireEvent, getByText, render } from '@testing-library/react';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { Product } from '../../types';
import '@testing-library/jest-dom/extend-expect';

jest.mock('../../hooks');

describe('MainPage test', () => {
    const currentTime = '18:10:16';
    jest.mocked(useCurrentTime).mockReturnValue(currentTime);

    const products: Product[] = [
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
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];
    jest.mocked(useProducts).mockReturnValue(products);

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should show correct time', () => {
        const { getByRole } = render(<MainPage />);
        expect(getByRole('heading', { level: 3 })).toHaveTextContent(
            currentTime
        );
    });

    it('should change products list when category is clicked', () => {
        const { queryByText, container } = render(<MainPage />);
        const categoriesContainer = container.querySelector('.categories');
        fireEvent.click(
            getByText(categoriesContainer as HTMLElement, 'Одежда')
        );

        expect(container.querySelectorAll('.product-card').length).toEqual(1);
        expect(queryByText('Костюм гуся')).toBeInTheDocument;
    });
});

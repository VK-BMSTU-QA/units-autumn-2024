import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime } from '../../hooks';
import { updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime.ts', () => ({
    useCurrentTime: () => '00:00:00',
}));

jest.mock('../../utils/updateCategories.ts', () => ({
    updateCategories: jest.fn(),
}));

describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should update categories when a category is clicked', () => {
        (updateCategories as jest.Mock).mockReturnValue(['Электроника'])

        const rendered = render(<MainPage />);

        const categoryButton = rendered.getAllByText('Электроника')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        
        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
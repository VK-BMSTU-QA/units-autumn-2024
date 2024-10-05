import { useCurrentTime } from '../useCurrentTime';
import { act, renderHook } from '@testing-library/react';

jest.useFakeTimers();
afterEach(jest.clearAllMocks);

describe('test use products function', () => {
    it('should return mocked time', () => {
        const mockedDateData = '2024-10-05T09:33:21'
        
        const mockDateReturn = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue(mockedDateData);

        const { result } = renderHook(useCurrentTime);

        expect(mockDateReturn).toBeCalledTimes(1);
        expect(result.current).toBe(mockedDateData);
    });

    it('should increment current time after one second', () => {
        const intervalPeriod = 1000;
        const mockDateLocaleString = 'date locale';
        const updatedMockDateLocaleString = 'new date locale';

        let mockDateLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue(mockDateLocaleString);

        setTimeout(() => {
            mockDateLocale = mockDateLocale.mockReturnValue(
                updatedMockDateLocaleString
            );
        }, intervalPeriod);

        const { result } = renderHook(useCurrentTime);

        expect(result.current).toBe(mockDateLocaleString);

        act(() => {
            jest.advanceTimersByTime(intervalPeriod);
        });

        expect(result.current).toBe(updatedMockDateLocaleString);
    });

    
});
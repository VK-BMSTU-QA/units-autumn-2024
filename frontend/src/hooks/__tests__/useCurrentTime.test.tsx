import { useCurrentTime } from '../useCurrentTime';
import { cleanup, renderHook, act } from '@testing-library/react';

jest.mock('..');
jest.useFakeTimers();

describe('test use current time function', () => {
    afterEach(() => {
        cleanup;
        jest.clearAllMocks();
    });
    it('should return fake previously setted time', () => {
        const mockToLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue('2020-01-01T01:00:00');

        expect(mockToLocale).toHaveBeenCalledTimes(0);

        const { result } = renderHook(() => useCurrentTime());

        expect(mockToLocale).toHaveBeenCalledTimes(1);
        expect(result.current).toEqual('2020-01-01T01:00:00');
    });
    it('should update fake previously setted time', () => {
        let mockToLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue('2020-01-01T01:00:00');

        expect(mockToLocale).toHaveBeenCalledTimes(0);

        const { result } = renderHook(() => useCurrentTime());

        expect(mockToLocale).toHaveBeenCalledTimes(1);
        mockToLocale = mockToLocale.mockReturnValue('new mock locale');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(mockToLocale).toHaveBeenCalledTimes(3); //3 - потому что происходит переприсваивание mockToLocale
        expect(result.current).toEqual('new mock locale');
    });
});

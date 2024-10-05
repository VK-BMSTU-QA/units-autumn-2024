import { act, renderHook } from "@testing-library/react";
import { useCurrentTime } from "./useCurrentTime";

describe('test for the current time function', () => {
    beforeAll(()=>{
        jest.useFakeTimers();
    });
    afterAll(()=>{
        jest.useRealTimers();
    })
    it('return current time', () => {
        const testingTime = renderHook(() => useCurrentTime());
        const expectedTime = new Date().toLocaleTimeString('ru-RU');
        expect(testingTime.result.current).toBe(expectedTime);
    });

    it('update every second', () => {
        const testingTime = renderHook(() => useCurrentTime());
        const resultSecond = testingTime.result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        const resultSecond1 = testingTime.result.current;
        expect(resultSecond).not.toBe(resultSecond1);
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        const resultSecond2 = testingTime.result.current;
        expect(resultSecond1).not.toBe(resultSecond2);
    });
});
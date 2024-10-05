import {renderHook} from "@testing-library/react";
import {useCurrentTime} from "../useCurrentTime";

jest.useFakeTimers();
afterEach(jest.clearAllMocks);

describe('test useCurrentTime hook', () => {
    it('should return the current time in right format', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);
    });


    it('should have clearInterval been called once time', () => {
        const { result, unmount } = renderHook(() => useCurrentTime());
        jest.spyOn(global, 'clearInterval');
        unmount();
        expect(clearInterval).toHaveBeenCalledTimes(1);
    });
});
import os
import subprocess
import sys
import re

def run_sanity_check():
    print("Starting Sanity Check for All PAs...\n")
    failed_tests = []
    passed_tests = []

    # Find all directories that look like PA<number>
    # We sort them to run in order (PA1, PA2, PA3...)
    items = os.listdir('.')
    pa_dirs = []
    for item in items:
        if os.path.isdir(item) and re.match(r'^PA\d+$', item):
            pa_dirs.append(item)
    
    # Sort by the numeric part
    pa_dirs.sort(key=lambda x: int(x[2:]))

    for pa_dir in pa_dirs:
        test_file = os.path.join(pa_dir, "Test.py")
        reference_file = os.path.join("ReferenceAnswers", f"{pa_dir}_Answer.py")

        if not os.path.exists(test_file):
            print(f"[{pa_dir}] SKIPPED: Test file not found at {test_file}")
            continue
        
        if not os.path.exists(reference_file):
            print(f"[{pa_dir}] SKIPPED: Reference file not found at {reference_file}")
            continue

        print(f"[{pa_dir}] Running {test_file} against {reference_file}...")
        
        try:
            # Run the test script with the reference file as an argument
            result = subprocess.run(
                [sys.executable, test_file, reference_file],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"[{pa_dir}] PASSED ✅")
                passed_tests.append(pa_dir)
            else:
                print(f"[{pa_dir}] FAILED ❌")
                print("--- Error Output ---")
                print(result.stderr)
                print("--------------------")
                failed_tests.append(pa_dir)

        except Exception as e:
            print(f"[{pa_dir}] ERROR: {str(e)}")
            failed_tests.append(pa_dir)
        
        print("-" * 40)

    print("\nSUMMARY")
    print(f"Passed: {len(passed_tests)} ({', '.join(passed_tests)})")
    print(f"Failed: {len(failed_tests)} ({', '.join(failed_tests)})")

    if failed_tests:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    run_sanity_check()

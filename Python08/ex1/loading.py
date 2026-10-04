import importlib
import importlib.util


def check_dependencies(packages_name: str, description: str) -> None:
    spec = importlib.util.find_spec(packages_name)
    if spec is None:
        print(f'[MISSING] {packages_name} - Not installed')
    else:
        module = importlib.import_module(packages_name)
        version = module.__version__
        print(f'[OK] {packages_name} ({version}) - {description}')


if __name__ == "__main__":
    print('\nLOADING STATUS: Loading programs...\n')

    print('Checking dependencies')
    check_dependencies('pandas', 'Data manipulation ready')
    check_dependencies('numpy', 'Numerical computations ready')
    check_dependencies('matplotlib', 'Visualization ready')

    print('\nAnalyzing Matrix data...')

    np = importlib.import_module('numpy')
    pd = importlib.import_module('pandas')
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=['Value'])

    print('Processing 1000 data points...')
    print('Generating visualization...')

    plt = importlib.import_module('matplotlib.pyplot')
    plt.hist(df['Value'], bins=50)
    plt.savefig('matrix_analysis.png')

    print('\nAnalysis complete!')
    print('Results saved to matrix_analysis.png')

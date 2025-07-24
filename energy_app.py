import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="World Energy Consumption Dashboard",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 World Energy Consumption Dashboard")
st.markdown("Analyze global energy consumption patterns and trends using real-world data")

# Cache the data loading function
@st.cache_data
def load_energy_data():
    """Load the energy consumption dataset"""
    try:
        # You'll need to upload the CSV file to your project directory
        # Download from: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption/data
        df = pd.read_csv('World Energy Consumption.csv')
        
        # Clean and prepare the data
        df = df.dropna(subset=['country'])
        
        # Convert year to datetime for better plotting
        df['year'] = pd.to_datetime(df['year'], format='%Y')
        
        # Fill missing values with 0 for energy consumption columns
        energy_columns = [
            'coal_consumption', 'gas_consumption', 'oil_consumption',
            'nuclear_consumption', 'hydro_consumption', 'wind_consumption',
            'solar_consumption', 'other_renewable_consumption',
            'primary_energy_consumption', 'electricity_generation'
        ]
        
        for col in energy_columns:
            if col in df.columns:
                df[col] = df[col].fillna(0)
        
        return df
    
    except FileNotFoundError:
        st.error("❌ Dataset not found! Please download 'World Energy Consumption.csv' from Kaggle and place it in your project directory.")
        st.markdown("""
        ### 📥 How to get the dataset:
        1. Go to: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption/data
        2. Download the CSV file
        3. Place it in the same folder as this Python file
        4. Refresh the page
        """)
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def create_sample_data():
    """Create sample data if the real dataset is not available"""
    countries = ['United States', 'China', 'India', 'Germany', 'Japan', 'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia']
    years = list(range(2000, 2023))
    
    data = []
    np.random.seed(42)
    
    for country in countries:
        base_consumption = np.random.uniform(50, 500)  # Base consumption level
        growth_rate = np.random.uniform(-0.02, 0.05)  # Annual growth rate
        
        for i, year in enumerate(years):
            # Simulate growth over time with some randomness
            consumption = base_consumption * (1 + growth_rate) ** i * np.random.uniform(0.9, 1.1)
            
            data.append({
                'country': country,
                'year': pd.to_datetime(str(year), format='%Y'),
                'primary_energy_consumption': max(consumption, 0),
                'coal_consumption': max(consumption * 0.3 * np.random.uniform(0.8, 1.2), 0),
                'gas_consumption': max(consumption * 0.25 * np.random.uniform(0.8, 1.2), 0),
                'oil_consumption': max(consumption * 0.3 * np.random.uniform(0.8, 1.2), 0),
                'nuclear_consumption': max(consumption * 0.1 * np.random.uniform(0.5, 1.5), 0),
                'hydro_consumption': max(consumption * 0.05 * np.random.uniform(0.5, 2.0), 0),
                'wind_consumption': max(consumption * 0.03 * np.random.uniform(0, 3.0), 0),
                'solar_consumption': max(consumption * 0.02 * np.random.uniform(0, 4.0), 0),
                'other_renewable_consumption': max(consumption * 0.02 * np.random.uniform(0.5, 2.0), 0),
                'electricity_generation': max(consumption * 0.4 * np.random.uniform(0.9, 1.1), 0),
                'gdp': consumption * np.random.uniform(20, 100),
                'population': np.random.uniform(1e6, 1e9)
            })
    
    return pd.DataFrame(data)

def calculate_energy_metrics(df):
    """Calculate key energy metrics"""
    latest_year = df['year'].max()
    latest_data = df[df['year'] == latest_year]
    
    total_consumption = latest_data['primary_energy_consumption'].sum()
    avg_consumption = latest_data['primary_energy_consumption'].mean()
    
    # Calculate renewable percentage
    renewable_cols = ['hydro_consumption', 'wind_consumption', 'solar_consumption', 'other_renewable_consumption']
    renewable_total = 0
    fossil_total = 0
    
    for col in renewable_cols:
        if col in latest_data.columns:
            renewable_total += latest_data[col].sum()
    
    fossil_cols = ['coal_consumption', 'gas_consumption', 'oil_consumption']
    for col in fossil_cols:
        if col in latest_data.columns:
            fossil_total += latest_data[col].sum()
    
    renewable_percentage = (renewable_total / (renewable_total + fossil_total)) * 100 if (renewable_total + fossil_total) > 0 else 0
    
    return {
        'total_consumption': total_consumption,
        'avg_consumption': avg_consumption,
        'renewable_percentage': renewable_percentage,
        'countries_count': len(latest_data)
    }

def display_overview_metrics(df):
    """Display key metrics in the overview section"""
    metrics = calculate_energy_metrics(df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Global Energy Consumption",
            f"{metrics['total_consumption']:,.0f} TWh",
            help="Total primary energy consumption globally"
        )
    
    with col2:
        st.metric(
            "Average per Country",
            f"{metrics['avg_consumption']:,.0f} TWh",
            help="Average energy consumption per country"
        )
    
    with col3:
        st.metric(
            "Renewable Energy Share",
            f"{metrics['renewable_percentage']:.1f}%",
            help="Percentage of renewable energy in total consumption"
        )
    
    with col4:
        st.metric(
            "Countries Analyzed",
            f"{metrics['countries_count']}",
            help="Number of countries in the dataset"
        )

def create_consumption_trends(df, selected_countries):
    """Create energy consumption trends chart"""
    
    # Filter data for selected countries
    filtered_df = df[df['country'].isin(selected_countries)]
    
    fig = px.line(
        filtered_df,
        x='year',
        y='primary_energy_consumption',
        color='country',
        title='Energy Consumption Trends Over Time',
        labels={
            'primary_energy_consumption': 'Energy Consumption (TWh)',
            'year': 'Year'
        }
    )
    
    fig.update_layout(
        height=500,
        hovermode='x unified'
    )
    
    return fig

def create_energy_mix_chart(df, selected_country, selected_year):
    """Create energy mix pie chart for a specific country and year"""
    
    # Filter data
    country_data = df[(df['country'] == selected_country) & (df['year'].dt.year == selected_year)]
    
    if country_data.empty:
        return None
    
    # Prepare energy mix data
    energy_sources = {
        'Coal': country_data['coal_consumption'].iloc[0] if 'coal_consumption' in country_data.columns else 0,
        'Natural Gas': country_data['gas_consumption'].iloc[0] if 'gas_consumption' in country_data.columns else 0,
        'Oil': country_data['oil_consumption'].iloc[0] if 'oil_consumption' in country_data.columns else 0,
        'Nuclear': country_data['nuclear_consumption'].iloc[0] if 'nuclear_consumption' in country_data.columns else 0,
        'Hydro': country_data['hydro_consumption'].iloc[0] if 'hydro_consumption' in country_data.columns else 0,
        'Wind': country_data['wind_consumption'].iloc[0] if 'wind_consumption' in country_data.columns else 0,
        'Solar': country_data['solar_consumption'].iloc[0] if 'solar_consumption' in country_data.columns else 0,
        'Other Renewables': country_data['other_renewable_consumption'].iloc[0] if 'other_renewable_consumption' in country_data.columns else 0
    }
    
    # Remove zero values
    energy_sources = {k: v for k, v in energy_sources.items() if v > 0}
    
    if not energy_sources:
        return None
    
    fig = px.pie(
        values=list(energy_sources.values()),
        names=list(energy_sources.keys()),
        title=f'Energy Mix - {selected_country} ({selected_year})',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=500)
    
    return fig

def create_top_consumers_chart(df, year, top_n=10):
    """Create top energy consumers chart"""
    
    year_data = df[df['year'].dt.year == year].nlargest(top_n, 'primary_energy_consumption')
    
    fig = px.bar(
        year_data,
        x='primary_energy_consumption',
        y='country',
        orientation='h',
        title=f'Top {top_n} Energy Consumers ({year})',
        labels={
            'primary_energy_consumption': 'Energy Consumption (TWh)',
            'country': 'Country'
        },
        color='primary_energy_consumption',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
    
    return fig

def create_renewable_growth_chart(df, selected_countries):
    """Create renewable energy growth chart"""
    
    # Calculate total renewable energy
    renewable_cols = ['hydro_consumption', 'wind_consumption', 'solar_consumption', 'other_renewable_consumption']
    
    filtered_df = df[df['country'].isin(selected_countries)].copy()
    
    # Sum all renewable sources
    filtered_df['total_renewable'] = 0
    for col in renewable_cols:
        if col in filtered_df.columns:
            filtered_df['total_renewable'] += filtered_df[col].fillna(0)
    
    fig = px.line(
        filtered_df,
        x='year',
        y='total_renewable',
        color='country',
        title='Renewable Energy Growth Over Time',
        labels={
            'total_renewable': 'Renewable Energy Consumption (TWh)',
            'year': 'Year'
        }
    )
    
    fig.update_layout(height=500)
    
    return fig

def main():
    # Load data
    df = load_energy_data()
    
    if df is None:
        st.info("📊 Using sample data for demonstration. Download the real dataset for actual analysis!")
        df = create_sample_data()
    
    # Sidebar controls
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Country selection
    available_countries = sorted(df['country'].unique())
    selected_countries = st.sidebar.multiselect(
        "Select Countries for Analysis:",
        available_countries,
        default=available_countries[:5] if len(available_countries) >= 5 else available_countries
    )
    
    # Year range selection
    min_year = int(df['year'].dt.year.min())
    max_year = int(df['year'].dt.year.max())
    
    selected_year_range = st.sidebar.slider(
        "Select Year Range:",
        min_year,
        max_year,
        (max_year - 10, max_year)
    )
    
    # Filter data based on selections
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['year'].dt.year >= selected_year_range[0]) &
        (df['year'].dt.year <= selected_year_range[1])
    ]
    
    # Main dashboard
    if not selected_countries:
        st.warning("👆 Please select at least one country from the sidebar!")
        return
    
    # Overview metrics
    st.header("📊 Global Energy Overview")
    display_overview_metrics(df)
    
    # Charts section
    st.header("📈 Energy Consumption Analysis")
    
    # Row 1: Consumption trends and energy mix
    col1, col2 = st.columns(2)
    
    with col1:
        trends_fig = create_consumption_trends(filtered_df, selected_countries)
        st.plotly_chart(trends_fig, use_container_width=True)
    
    with col2:
        # Energy mix for single country
        if len(selected_countries) >= 1:
            mix_country = st.selectbox("Select country for energy mix:", selected_countries)
            mix_year = st.selectbox("Select year for energy mix:", 
                                  sorted(df['year'].dt.year.unique(), reverse=True))
            
            mix_fig = create_energy_mix_chart(df, mix_country, mix_year)
            if mix_fig:
                st.plotly_chart(mix_fig, use_container_width=True)
            else:
                st.info("No energy mix data available for selected country/year")
    
    # Row 2: Top consumers and renewable growth
    col1, col2 = st.columns(2)
    
    with col1:
        top_year = st.selectbox("Year for top consumers:", 
                              sorted(df['year'].dt.year.unique(), reverse=True),
                              key="top_consumers_year")
        top_consumers_fig = create_top_consumers_chart(df, top_year)
        st.plotly_chart(top_consumers_fig, use_container_width=True)
    
    with col2:
        renewable_fig = create_renewable_growth_chart(filtered_df, selected_countries)
        st.plotly_chart(renewable_fig, use_container_width=True)
    
    # Data table
    st.header("📋 Detailed Data")
    
    # Show latest year data
    latest_year = df['year'].max()
    latest_data = df[df['year'] == latest_year]
    
    display_columns = ['country', 'primary_energy_consumption', 'coal_consumption', 
                      'gas_consumption', 'oil_consumption', 'nuclear_consumption',
                      'hydro_consumption', 'wind_consumption', 'solar_consumption']
    
    # Only show columns that exist in the dataset
    available_display_columns = [col for col in display_columns if col in latest_data.columns]
    
    if selected_countries:
        table_data = latest_data[latest_data['country'].isin(selected_countries)][available_display_columns]
        st.dataframe(table_data.round(2), use_container_width=True)
    
    # Insights section
    st.header("💡 Key Insights")
    
    # Calculate some insights
    if not filtered_df.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🏆 Highest Consumer")
            top_consumer = filtered_df.loc[filtered_df['primary_energy_consumption'].idxmax()]
            st.write(f"**{top_consumer['country']}**")
            st.write(f"{top_consumer['primary_energy_consumption']:,.0f} TWh")
            st.write(f"Year: {top_consumer['year'].year}")
        
        with col2:
            st.subheader("📈 Fastest Growing")
            # Calculate growth rate for each country
            growth_rates = []
            for country in selected_countries:
                country_data = filtered_df[filtered_df['country'] == country].sort_values('year')
                if len(country_data) >= 2:
                    first_year = country_data.iloc[0]['primary_energy_consumption']
                    last_year = country_data.iloc[-1]['primary_energy_consumption']
                    if first_year > 0:
                        growth_rate = ((last_year / first_year) ** (1/len(country_data)) - 1) * 100
                        growth_rates.append((country, growth_rate))
            
            if growth_rates:
                fastest_growing = max(growth_rates, key=lambda x: x[1])
                st.write(f"**{fastest_growing[0]}**")
                st.write(f"{fastest_growing[1]:.1f}% annual growth")
        
        with col3:
            st.subheader("🌱 Most Renewable")
            latest_data_filtered = df[df['year'] == df['year'].max()]
            
            renewable_percentages = []
            for country in selected_countries:
                country_data = latest_data_filtered[latest_data_filtered['country'] == country]
                if not country_data.empty:
                    renewable_cols = ['hydro_consumption', 'wind_consumption', 'solar_consumption', 'other_renewable_consumption']
                    fossil_cols = ['coal_consumption', 'gas_consumption', 'oil_consumption']
                    
                    renewable_total = sum(country_data[col].iloc[0] for col in renewable_cols if col in country_data.columns)
                    fossil_total = sum(country_data[col].iloc[0] for col in fossil_cols if col in country_data.columns)
                    
                    if renewable_total + fossil_total > 0:
                        renewable_pct = (renewable_total / (renewable_total + fossil_total)) * 100
                        renewable_percentages.append((country, renewable_pct))
            
            if renewable_percentages:
                most_renewable = max(renewable_percentages, key=lambda x: x[1])
                st.write(f"**{most_renewable[0]}**")
                st.write(f"{most_renewable[1]:.1f}% renewable")
    
    # Footer
    st.markdown("---")
    st.caption(f"Data source: World Energy Consumption Dataset | Last updated: {df['year'].max().strftime('%Y')}")

if __name__ == "__main__":
    main()
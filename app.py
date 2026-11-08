import matplotlib.pyplot as plt
import numpy as np

# Set IEEE-style plot parameters (clean, legible, serif fonts if available)
plt.rcParams.update({'font.size': 12, 'figure.figsize': (8, 5)})

# ==========================================
# FIGURE 4: Router Confidence Scatter Plot
# ==========================================
def generate_figure_4():
    # Synthetic data matching the 20-question benchmark narrative
    queries = np.arange(1, 21)
    
    # In-domain scores (above 0.75)
    local_x = [1, 2, 4, 7, 8, 10, 14, 15, 18, 19]
    local_y = [0.90, 0.88, 0.82, 0.78, 0.95, 0.85, 0.89, 0.77, 0.91, 0.81]
    
    # Out-of-domain scores (below 0.75)
    cloud_x = [3, 5, 6, 9, 11, 12, 13, 16, 17, 20]
    cloud_y = [0.45, 0.62, 0.55, 0.71, 0.30, 0.68, 0.40, 0.58, 0.65, 0.42]

    plt.figure()
    plt.scatter(local_x, local_y, color='black', marker='o', s=80, label='Local RAG (In-Domain)')
    plt.scatter(cloud_x, cloud_y, color='gray', marker='x', s=80, label='Cloud Fallback (Out-of-Domain)')
    
    # Draw the Decision Boundary
    plt.axhline(y=0.75, color='black', linestyle='--', linewidth=2, label=r'Decision Boundary ($\tau = 0.75$)')
    
    plt.xlabel('Benchmark Query Index')
    plt.ylabel('Calibrated Similarity Score ($S_{cal}$)')
    plt.title('Fig. 6: Pre-Generation Semantic Routing Decision Boundary')
    plt.ylim(0, 1.05)
    plt.xticks(np.arange(1, 21, step=2))
    plt.legend(loc='lower right')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('figure_4_scatter.svg', format='svg')
    print("Figure 4 saved as figure_4_scatter.svg")

# ==========================================
# FIGURE 5: End-to-End Latency Bar Chart
# ==========================================
def generate_figure_5():
    # Data from Section IV.C
    labels = ['Pre-Gen: Local RAG', 'Pre-Gen: Cloud Fallback', 'Post-Gen Baseline (CRAG)']
    means = [1913, 1860, 3750]
    medians = [2422, 1851, 3810]

    x = np.arange(len(labels))
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, means, width, label='Mean Latency', color='dimgray', edgecolor='black')
    rects2 = ax.bar(x + width/2, medians, width, label='Median Latency', color='lightgray', edgecolor='black')

    ax.set_ylabel('Latency (Milliseconds)')
    ax.set_title('Fig. 7: End-to-End System Latency by Routing Architecture')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.grid(axis='y', linestyle=':', alpha=0.6)

    # Attach text labels above bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.tight_layout()
    plt.savefig('figure_5_latency.svg', format='svg')
    print("Figure 5 saved as figure_5_latency.svg")

# Run the functions
generate_figure_4()
generate_figure_5()
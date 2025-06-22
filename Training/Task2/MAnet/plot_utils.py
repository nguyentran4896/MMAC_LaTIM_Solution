import matplotlib.pyplot as plt
import os

def plot_training_progress(logs, save_path, title="Training Progress"):
    """
    Plots and saves the training and validation loss and dice curves.
    Args:
        logs: dict with keys 'train_loss', 'val_loss', 'train_dice', 'val_dice', each a list of values per epoch
        save_path: path to save the plot image
        title: plot title
    """
    plt.figure(figsize=(10, 5))
    epochs = range(1, len(logs['train_loss']) + 1)
    
    plt.subplot(1, 2, 1)
    plt.plot(epochs, logs['train_loss'], label='Train Loss')
    if 'val_loss' in logs:
        plt.plot(epochs, logs['val_loss'], label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(epochs, logs['train_dice'], label='Train Dice')
    if 'val_dice' in logs:
        plt.plot(epochs, logs['val_dice'], label='Val Dice')
    plt.xlabel('Epoch')
    plt.ylabel('Dice')
    plt.title('Dice')
    plt.legend()
    
    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close() 
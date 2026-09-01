from client import PagedAttentionVirtualMemoryAllocatorClient

def main():
    client = PagedAttentionVirtualMemoryAllocatorClient()
    res = client.allocate_kv_virtual_blocks(256, 16, 4096)
    print('PagedAttention Allocator: ' + res['allocator_cycle_id'] + ' (' + str(res['active_streams']) + ' streams)')
    print('Block Hit Ratio: ' + str(res['virtual_block_hit_ratio_pct']) + '% | Fragmentation: ' + str(res['internal_memory_fragmentation_pct']) + '%')
    print('Throughput Gain: ' + str(res['kv_cache_throughput_gain_x']) + 'x | CUDA Memory Saved: ' + str(res['cuda_memory_saved_gb']) + ' GB')

if __name__ == '__main__':
    main()

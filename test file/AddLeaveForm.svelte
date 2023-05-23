<div class="flex items-center justify-center h-fit mb-1 rounded bg-gray-50 dark:bg-gray-800">
	<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 table-auto">
		<thead class="text-m  text-gray-700 border-b bg-gray-200 dark:bg-gray-700 dark:text-gray-400">
			<tr>
				<th scope="col" class="pl-6">
					CODE
					<Sort on:click={() => handleSort('code')}/>
				</th>
				<th scope="col" class="pl-6">
					DESCRIPTION
					<Sort on:click={() => handleSort('description')} />
				</th>
				<th scope="col" class="pl-6">
					GROUP TYPE
					<Sort on:click={() => handleSort('grouptype')} />
				</th>
				<th scope="col" class="pl-6">
					DATE TYPE 
					<Sort on:click={() => handleSort('datetype')} />		
				</th>
				<th scope="col" class="pl-6">
					MAX DAYS 
					<Sort on:click={() => handleSort('maxday')} />		
				</th>
				<th scope="col" class="pl-6">
					DATE BEFORE FILING 
					<Sort on:click={() => handleSort('dbfiling')} />		
				</th>
				<th scope="col" class="pl-6">
					STATUS		
				</th>
				<th scope="col" class="pl-6">
					<div class="flex gap-2 w-max">
						<label for="items" class="block text-m font-semibold text-gray-900 dark:text-white"
							>No. of Entries</label
						>
						<input
							type="number"
							id="items"
							bind:value={pageSize}
							on:change={handleOverFlow}
							class="w-16 h-4 text-sm text-center text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600"
							placeholder=" "
						/>
					</div>
				</th>
			</tr>
		</thead>
		<tbody>
			{#key paginatedItems}
				{#if paginatedItems.length}
					{#each paginatedItems as leave}
						<tr
							class=" bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
							on:mouseenter={() => {
								if (currentLeave !== leave) {
									currentLeave = leave;
								}
							}}
						>
							<td
								class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium"
							>
								{leave.code || ''}
							</td>
							<td class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium">
								{leave.description || ''}
							</td>
							<td class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium">
								{leave.grouptype || ''}
							</td>
							<td class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium">
								{leave.datetype || ''}
							</td>
							<td class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium">
								{leave.maxday || ''}
							</td>
							<td class="px-6 py-4 text-gray-700 whitespace-nowrap dark:text-white text-m font-medium">
								{dateToString(leave.dbfiling) || ''}
							</td>
							<td class="flex items-center px-6 py-4">
								<div class="flex items-center ">
									<div
										class={leave.isActive
											? 'h-2.5 w-2.5 rounded-full bg-green-500 mr-2'
											: 'h-2.5 w-2.5 rounded-full bg-red-500 mr-2'}
									/>
									<div class="text-sm text-gray-700 font-medium">
										{leave.isActive ? 'Active' : 'Inactive'}
									</div>
								</div>
							</td>
							<td class="px-6 py-4 col-span-3">
								<Button
									extraClasses="mx-1 pr-2 pl-4 inline-flex items-center text-center font-semibold rounded-full"
									textSize="text-m"
									hoverTitle="Edit"
									textColor="text-white"
									bgColor="bg-blue-700"
									bgColorHover="bg-blue-800"
									on:click={handleEditLeaveModal}
								>
									<svg
										class="w-5 h-5 mr-2 dark:text-gray-400"
										fill="currentColor"
										viewBox="0 0 24 24"
										aria-hidden="true"
									>
										<path
											d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-8.4 8.4a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32l8.4-8.4z"
										/>
										<path
											d="M5.25 5.25a3 3 0 00-3 3v10.5a3 3 0 003 3h10.5a3 3 0 003-3V13.5a.75.75 0 00-1.5 0v5.25a1.5 1.5 0 01-1.5 1.5H5.25a1.5 1.5 0 01-1.5-1.5V8.25a1.5 1.5 0 011.5-1.5h5.25a.75.75 0 000-1.5H5.25z"
										/>
									</svg></Button
								>
								<Button
									extraClasses="mx-1 pr-2 pl-4 inline-flex items-center text-center font-semibold rounded-full"
									textSize="text-m"
									hoverTitle="Delete"
									textColor="text-white"
									bgColor="bg-red-600"
									bgColorHover="bg-red-700"
									on:click={handleConfirmDeleteModal}
								>
									<svg
										class="w-5 h-5 mr-2 dark:text-gray-400 "
										fill="currentColor"
										viewBox="0 0 24 24"
										aria-hidden="true"
									>
										<path
											clip-rule="evenodd"
											fill-rule="evenodd"
											d="M16.5 4.478v.227a48.816 48.816 0 013.878.512.75.75 0 11-.256 1.478l-.209-.035-1.005 13.07a3 3 0 01-2.991 2.77H8.084a3 3 0 01-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 01-.256-1.478A48.567 48.567 0 017.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 013.369 0c1.603.051 2.815 1.387 2.815 2.951zm-6.136-1.452a51.196 51.196 0 013.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 00-6 0v-.113c0-.794.609-1.428 1.364-1.452zm-.355 5.945a.75.75 0 10-1.5.058l.347 9a.75.75 0 101.499-.058l-.346-9zm5.48.058a.75.75 0 10-1.498-.058l-.347 9a.75.75 0 001.5.058l.345-9z"
										/>
									</svg>
								</Button>
							</td>
						</tr>
					{/each}
				{/if}
			{/key}
		</tbody>
		<div class="flex flex-col items-center mt-2">
			<span class="text-sm text-gray-700 dark:text-gray-400">
				Showing <span class="font-semibold text-gray-900 dark:text-white">{pageMinIndex}</span> to
				<span class="font-semibold text-gray-900 dark:text-white">{pageMaxIndex}</span>
				of <span class="font-semibold text-gray-900 dark:text-white">{itemSize}</span> Entries
			</span>
			<div class="inline-flex mt-2 xs:mt-0">
				<button
					on:click={decrementPageNumber}
					class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
				>
					<svg aria-hidden="true" class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
						<path
							fill-rule="evenodd"
							d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z"
							clip-rule="evenodd"
						/>
					</svg>
					Prev
				</button>
				<button
					on:click={incrementPageNumber}
					class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 border-0 border-l border-gray-700 rounded-r hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
				>
					Next
					<svg aria-hidden="true" class="w-5 h-5 ml-2" fill="currentColor" viewBox="0 0 20 20">
						<path
							fill-rule="evenodd"
							d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/>
					</svg>
				</button>
			</div>
		</div>
	</table>
</div>